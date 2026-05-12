





import java.util.List;
import java.util.ArrayList;

public class Game_Start_external  {






    private Computer_Turn_external computer_turn_external;




    private Roll_Dice_external roll_dice_external;




    private Roll_First_external roll_first_external;




    private Player_Actor player_actor;


    public Game_Start_external(
    ) {
    }



    public Computer_Turn_external getComputer_turn_external() {
        return computer_turn_external;
    }

    public void setComputer_turn_external(Computer_Turn_external computer_turn_external) {
        this.computer_turn_external = computer_turn_external;
    }
    public Roll_Dice_external getRoll_dice_external() {
        return roll_dice_external;
    }

    public void setRoll_dice_external(Roll_Dice_external roll_dice_external) {
        this.roll_dice_external = roll_dice_external;
    }
    public Roll_First_external getRoll_first_external() {
        return roll_first_external;
    }

    public void setRoll_first_external(Roll_First_external roll_first_external) {
        this.roll_first_external = roll_first_external;
    }
    public Player_Actor getPlayer_actor() {
        return player_actor;
    }

    public void setPlayer_actor(Player_Actor player_actor) {
        this.player_actor = player_actor;
    }

}