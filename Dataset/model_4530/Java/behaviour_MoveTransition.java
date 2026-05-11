





import java.util.List;
import java.util.ArrayList;

public class behaviour_MoveTransition  {

    private boolean fluid;





    private behaviour_Slot behaviour_slot;




    private behaviour_Move behaviour_move;




    private behaviour_Move behaviour_move;




    private behaviour_Drone behaviour_drone;


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

    public behaviour_Slot getBehaviour_slot() {
        return behaviour_slot;
    }

    public void setBehaviour_slot(behaviour_Slot behaviour_slot) {
        this.behaviour_slot = behaviour_slot;
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
    public behaviour_Drone getBehaviour_drone() {
        return behaviour_drone;
    }

    public void setBehaviour_drone(behaviour_Drone behaviour_drone) {
        this.behaviour_drone = behaviour_drone;
    }

}