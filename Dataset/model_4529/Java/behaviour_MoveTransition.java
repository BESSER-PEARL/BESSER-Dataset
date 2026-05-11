





import java.util.List;
import java.util.ArrayList;

public class behaviour_MoveTransition  {

    private boolean fluid;





    private behaviour_Drone behaviour_drone;




    private behaviour_Move behaviour_move;




    private behaviour_Move behaviour_move;


    public behaviour_MoveTransition(
        boolean fluid    ) {
        this.fluid = fluid;
    }


    public boolean getFluid() {
        return fluid;
    }

    public void setFluid(boolean fluid) {
        this.fluid = fluid;
    }

    public behaviour_Drone getBehaviour_drone() {
        return behaviour_drone;
    }

    public void setBehaviour_drone(behaviour_Drone behaviour_drone) {
        this.behaviour_drone = behaviour_drone;
    }
    public behaviour_Move getBehaviour_move() {
        return behaviour_move;
    }

    public void setBehaviour_move(behaviour_Move behaviour_move) {
        this.behaviour_move = behaviour_move;
    }
    public behaviour_Move getBehaviour_move() {
        return behaviour_move;
    }

    public void setBehaviour_move(behaviour_Move behaviour_move) {
        this.behaviour_move = behaviour_move;
    }

}