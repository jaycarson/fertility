from Woman import Woman
import yaml
import argparse


class Simulation(object):
    def __init__(self, years, months, weight, height, carnivore, twins, casual_smoker, regular_smoker, end_year, ivf_allowed, size):
        years = int(years)
        months = int(months)
        end_year = int(end_year)
        self.duration = end_year * 12 - years * 12 - months
        self.sample_size = size

        chance_to_conceive = yaml.load(open('fertility.yml', 'r'), Loader=yaml.FullLoader)
        chance_to_miscarry = yaml.load(open('miscarriage.yml', 'r'), Loader=yaml.FullLoader)
        chance_on_ivf = yaml.load(open('ivf.yml', 'r'), Loader=yaml.FullLoader)

        self.population = []
        seed = 0
        for woman_id in range(0, self.sample_size):
            self.population.append(
                Woman(
                    years,
                    months,
                    weight,
                    height,
                    carnivore,
                    twins,
                    casual_smoker,
                    regular_smoker,
                    conceive = chance_to_conceive,
                    miscarry = chance_to_miscarry,
                    ivf = chance_on_ivf,
                    ivf_allowed = ivf_allowed,
                    seed = seed,
                )
            )
            seed += 1
        print('Age:          ' + str(years))
        print('Age End:      ' + str(end_year))
        print('Weight:       ' + str(weight))
        print('Height:       ' + str(height))
        print('BMI:          ' + str(self.population[0].bmi)[0:5])
        print('Carnivore:    ' + str(carnivore))
        print('Twins:        ' + str(twins))
        print('IVF Allowed:  ' + str(ivf_allowed))
        print('')

    def __call__(self):
        data = {}
        for period in range(0, self.duration):
            for woman in self.population:
                woman()
            total_children = 0
            total_miscarriages = 0
            total_still_births = 0
            total_children_with_down_syndrom = 0
            children_0 = 0
            children_1 = 0
            children_2 = 0
            children_3 = 0
            children_4 = 0
            children_5 = 0
            children_6 = 0
            children_7 = 0
            children_8 = 0
            children_9 = 0

            for woman in self.population:
                total_children += woman.children
                total_children_with_down_syndrom += woman.children_with_down_syndrom
                total_miscarriages += woman.miscarriages
                total_still_births += woman.still_births

                if woman.children == 0:
                    children_0 += 1
                elif woman.children == 1:
                    children_1 += 1
                elif woman.children == 2:
                    children_2 += 1
                elif woman.children == 3:
                    children_3 += 1
                elif woman.children == 4:
                    children_4 += 1
                elif woman.children == 5:
                    children_5 += 1
                elif woman.children == 6:
                    children_6 += 1
                elif woman.children == 7:
                    children_7 += 1
                elif woman.children == 8:
                    children_8 += 1
                elif woman.children >= 9:
                    children_9 += 1

            data[period] = {
                'year': period // 12,
                'month': period % 12,
                'children': total_children / self.sample_size,
                'children_with_down_syndrom': total_children_with_down_syndrom / self.sample_size,
                'miscarriages': total_miscarriages / self.sample_size,
                'still_births': total_still_births / self.sample_size,
                'children_0': children_0 / self.sample_size,
                'children_1': children_1 / self.sample_size,
                'children_2': children_2 / self.sample_size,
                'children_3': children_3 / self.sample_size,
                'children_4': children_4 / self.sample_size,
                'children_5': children_5 / self.sample_size,
                'children_6': children_6 / self.sample_size,
                'children_7': children_7 / self.sample_size,
                'children_8': children_8 / self.sample_size,
                'children_9': children_9 / self.sample_size,
            }

        #for period in range(0, self.duration):
        #    print(str(data[period]['year']) + ' ' + str(data[period]['month']) + ' ' + str(data[period]['children']) + ' ' + str(data[period]['miscarriages']))

        print('Children:                   ' + str(data[self.duration-1]['children']))
        print('Miscarriages:               ' + str(data[self.duration-1]['miscarriages']))
        print('Children With Down Syndrom: ' + str(data[self.duration-1]['children_with_down_syndrom']))
        print('Still Births:               ' + str(data[self.duration-1]['still_births']))
        print('')
        print('Children 0:   ' + str(data[self.duration-1]['children_0']))
        print('Children 1:   ' + str(data[self.duration-1]['children_1']))
        print('Children 2:   ' + str(data[self.duration-1]['children_2']))
        print('Children 3:   ' + str(data[self.duration-1]['children_3']))
        print('Children 4:   ' + str(data[self.duration-1]['children_4']))
        print('Children 5:   ' + str(data[self.duration-1]['children_5']))
        print('Children 6:   ' + str(data[self.duration-1]['children_6']))
        print('Children 7:   ' + str(data[self.duration-1]['children_7']))
        print('Children 8:   ' + str(data[self.duration-1]['children_8']))
        print('Children 9+:  ' + str(data[self.duration-1]['children_9']))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="""
            """,
        epilog="""
            """,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--years",
        default=35,
        help="Set starting age in years",
    )
    parser.add_argument(
        "--months",
        default=0,
        help="Set starting age in months",
    )
    parser.add_argument(
        "--weight",
        default=170,
        help="Set the weight of the subjects",
    )
    parser.add_argument(
        "--height",
        default=64,
        help="Set the height of the subjects.",
    )
    parser.add_argument(
        "--carnivore",
        action='store_true',
        help="Set whether the subjects primarily eat meat or not.",
    )
    parser.add_argument(
        "--twins",
        action='store_true',
        help="Set whether the subjects have twins running in the family.",
    )
    parser.add_argument(
        "--casual",
        action='store_true',
        help="Set whether the subjects are casual smokers or not.",
    )
    parser.add_argument(
        "--regular",
        action='store_true',
        help="Set whether the subjects are regular smokers or not.",
    )
    parser.add_argument(
        "--end",
        default=50,
        help="Set end year.",
    )
    parser.add_argument(
        "--ivf",
        action='store_false',
        help="Set whether IVF is allowed or not.",
    )
    parser.add_argument(
        "--size",
        default=1000000,
        help="Set sample size.",
    )
    parser.add_argument(
        "--tall",
        action='store_true',
        help="Set subjects to be tall (5'4''+).",
    )
    parser.add_argument(
        "--healthy",
        action='store_true',
        help="Set subjects to be have a healthy weight.",
    )
    parser.add_argument(
        "--morbid",
        action='store_true',
        help="Set subjects to be have a healthy weight.",
    )

    args = parser.parse_args()

    if args.tall:
        args.height = 65
    if args.healthy:
        args.weight = 130
    elif args.morbid:
        args.weight = 234

    app = Simulation(
        years = args.years,
        months = args.months,
        weight = args.weight,
        height = args.height,
        carnivore = args.carnivore,
        twins = args.twins,
        casual_smoker = args.casual,
        regular_smoker = args.regular,
        end_year = args.end,
        ivf_allowed = args.ivf,
        size = args.size,
    )
    app()
