def main():
    horse_total = 0
    player_total = 0
    player_real = 5.612
    runs = int(input("How many times do you want to take the average of? "))
    for _ in range(runs):
        player_total += float(input("How many blocks/second did the player sprint? "))
        horse_total += float(input("How many blocks/second did the horse run? "))
    player_average = player_total/runs
    horse_average = horse_total/runs
    factor = player_real/player_average
    horse_adjusted = horse_average * factor
    print(f'Horse average adjusted speed = {horse_adjusted:.4f}')

if __name__ == "__main__":
    main()
