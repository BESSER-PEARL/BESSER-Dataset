





import java.util.List;
import java.util.ArrayList;

public class Behaviour_Server extends Place {

    private int capacity;





    private Behaviour_PreTransitionConnection behaviour_pretransitionconnection;




    private Behaviour_WaitingLine behaviour_waitingline;




    private Behaviour_WaitingLine behaviour_waitingline;


    public Behaviour_Server(
        int capacity    ) {
        super(
        );
        this.capacity = capacity;
    }


    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }

    public Behaviour_PreTransitionConnection getBehaviour_pretransitionconnection() {
        return behaviour_pretransitionconnection;
    }

    public void setBehaviour_pretransitionconnection(Behaviour_PreTransitionConnection behaviour_pretransitionconnection) {
        this.behaviour_pretransitionconnection = behaviour_pretransitionconnection;
    }
    public Behaviour_WaitingLine getBehaviour_waitingline() {
        return behaviour_waitingline;
    }

    public void setBehaviour_waitingline(Behaviour_WaitingLine behaviour_waitingline) {
        this.behaviour_waitingline = behaviour_waitingline;
    }
    public Behaviour_WaitingLine getBehaviour_waitingline() {
        return behaviour_waitingline;
    }

    public void setBehaviour_waitingline(Behaviour_WaitingLine behaviour_waitingline) {
        this.behaviour_waitingline = behaviour_waitingline;
    }

}