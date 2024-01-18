import unittest
from unittest.mock import patch
from game.main import random_positions_on_edge, generate_obstacles, is_game_over, move_player, main, clear_screen


class TestGameLogic(unittest.TestCase):
    def setUp(self):
        # Ustawienia ogólne dla testów
        self.board_size = 10
        self.obstacle_number = 20
        self.start_pos = random_positions_on_edge(self.board_size, [])
        self.end_pos = random_positions_on_edge(self.board_size,
                                                ["N", "E", "W"] if self.start_pos[1] == 0 else ["S", "E", "W"])
        self.obstacles = generate_obstacles(self.board_size, self.obstacle_number, self.start_pos, self.end_pos)
        self.player_start_y, self.player_start_x = 0, 0
        self.movement_keys = {
            "up": b'H',
            "down": b'P',
            "left": b'K',
            "right": b'M'
        }

    @patch('game.main.msvcrt.getch')
    def test_user_interactions(self, mock_getch):
        # Symulacja naciśnięć klawiszy przez użytkownika
        mock_getch.side_effect = [b'K', b'M', b'H', b'P', b'q']

        player_y, player_x = 0, 0  # Przykładowa pozycja startowa
        board_size = 10
        obstacles = set()

        # Symulacja ruchu w lewo
        new_y, new_x = move_player(player_x, player_y, b'K', board_size, obstacles)
        self.assertEqual((new_y, new_x), (player_y, player_x - 1))

    def test_move_player_within_bounds_and_obstacles(self):
        # Symulacja pozycji gracza
        player_y, player_x = self.player_start_y, self.player_start_x

        # Symulacja przeszkód
        obstacles = self.obstacles

        # Test ruchu w górę - nie powinien wyjść poza planszę
        new_y, new_x = move_player(player_x, 0, self.movement_keys["up"], self.board_size, obstacles)
        self.assertEqual((new_y, new_x), (0, player_x))

        # Test ruchu w dół - nie powinien wyjść poza planszę
        new_y, new_x = move_player(player_x, self.board_size - 1, self.movement_keys["down"], self.board_size,
                                   obstacles)
        self.assertEqual((new_y, new_x), (self.board_size - 1, player_x))

        # Test ruchu w lewo - nie powinien wyjść poza planszę
        new_y, new_x = move_player(0, player_y, self.movement_keys["left"], self.board_size, obstacles)
        self.assertEqual((new_y, new_x), (player_y, 0))

        # Test ruchu w prawo - nie powinien wyjść poza planszę
        new_y, new_x = move_player(self.board_size - 1, player_y, self.movement_keys["right"], self.board_size,
                                   obstacles)
        self.assertEqual((new_y, new_x), (player_y, self.board_size - 1))

        # Test zapobiegania wchodzeniu na przeszkodę
        # Dodanie przeszkody bezpośrednio przed graczem
        obstacle_in_front = (player_y - 1, player_x)
        obstacles.add(obstacle_in_front)

        # Próba ruchu na przeszkodę - pozycja nie powinna się zmienić
        new_y, new_x = move_player(player_x, player_y, self.movement_keys["up"], self.board_size, obstacles)
        self.assertEqual((new_y, new_x), (player_y, player_x))

    def test_generate_obstacles_not_on_start_or_end(self):
        # Generowanie przeszkód z wykluczeniem pozycji startowej i końcowej
        start_pos = (self.start_y, self.start_x)
        end_pos = (self.end_y, self.end_x)
        obstacles = generate_obstacles(self.board_size, 20, start_pos, end_pos)

        # Sprawdzenie liczby wygenerowanych przeszkód
        self.assertEqual(len(obstacles), 20)

        # Sprawdzenie, czy przeszkody nie pojawiły się na pozycji startowej ani końcowej
        self.assertNotIn(start_pos, obstacles)
        self.assertNotIn(end_pos, obstacles)

        # Czy wszystkie przeszkody mieszczą się w granicach planszy
        for obstacle in obstacles:
            self.assertIn(obstacle[0], range(self.board_size))
            self.assertIn(obstacle[1], range(self.board_size))

    def test_game_over_conditions(self):
        # Test, gdy gracz nie jest na pozycji końcowej
        not_end_pos = (self.end_y - 1, self.end_x)  # Pozycja tuż przed końcową
        self.assertFalse(is_game_over(not_end_pos, (self.end_y, self.end_x)))

        # Test, gdy gracz jest na pozycji końcowej
        self.assertTrue(is_game_over((self.end_y, self.end_x), (self.end_y, self.end_x)))

        # Dodatkowe testy dla różnych pozycji gracza
        for y in range(self.board_size):
            for x in range(self.board_size):
                if (y, x) != (self.end_y, self.end_x):
                    self.assertFalse(is_game_over((y, x), (self.end_y, self.end_x)))


if __name__ == '__main__':
    unittest.main()