class Pizza():
    sizes = ['L', 'XL']

    def __init__(
        self,
        size: str,
        ingredients: list[str],
        emoji: str = '',
        is_delivered: bool = False,
        is_baked: bool = False,
        is_pickuped: bool = False
        ) -> None:
        """
        Describes a recipe of pizza
        Args:
        size: a size of pizza (L or XL)
        ingredients: the components of the recipe
        emoji: an emoji of pizza
        is_delivered: an indicator whether pizza is delivered or not
        is_baked: an indicator whether pizza is baked or not
        is_pickedup: an indicator whether pizza is picked up or not

        Raises:
            ValueError: if the size is invalid
        """
        if size not in self.sizes:
            raise ValueError(f'Invalid size: {size}')

        self.ingredients = ingredients
        self.ingredients = ingredients
        self.size = size
        self.emoji = emoji
        self.is_baked = is_baked
        self.is_delivered = is_delivered
        self.is_pickuped = is_pickuped

    def bake(self) -> None:
        """Bakes pizza"""
        self.is_baked = True

    def delivery(self) -> None:
        """Delivers pizza"""
        self.is_delivered = True

    def pickup(self) -> None:
        self.is_pickuped = True

    def __repr__(self) -> str:
        """String representation of a pizza recipe."""
        return f'Pizza({self.size}, {self.ingredients})'

    def __str__(self) -> str:
        """Returns a readable string representation of the pizza recipe."""
        return f'{self.size} pizza with {", ".join(self.ingredients)}'

    def __dict__(self) -> dict:
        """Returns a pizza recipe as a dictionary."""
        return {
            'size': self.size,
            'ingredients': self.ingredients,
        }

    def __eq__(self, other) -> bool:
        """Compares two pizzas by size & ingredients."""
        if not isinstance(other, Pizza):
            raise ValueError(f'Invalid pizza type: {type(other)}')
        return (
                self.size == other.size
                and self.ingredients == other.ingredients
        )

class Margherita(Pizza):
    """Margherita pizza recipe."""

    emoji = '🧀'
    ingredients = ['tomato sauce', 'mozzarella', 'tomatoes']

    def __init__(self, size: str = 'L') -> None:
        """Initializes a Margherita pizza recipe with a selected size."""

        super().__init__(size, self.ingredients, self.emoji)


class Pepperoni(Pizza):
    """Pepperoni pizza recipe."""

    emoji = '🍕'
    ingredients = ['tomato sauce', 'mozzarella', 'pepperoni']

    def __init__(self, size: str = 'L') -> None:
        """Initializes a Pepperoni pizza recipe with a selected size."""

        super().__init__(size, self.ingredients, self.emoji)


class Hawaiian(Pizza):
    """Hawaiian pizza recipe."""

    emoji = '🍍'
    ingredients = ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']

    def __init__(self, size: str = 'L') -> None:
        """Initializes a Hawaiian pizza recipe with a selected size."""

        super().__init__(size, self.ingredients, self.emoji)

