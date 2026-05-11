





import java.util.List;
import java.util.ArrayList;

public class Behaviour_QueuePlace extends Place {






    private Behaviour_WaitingLine behaviour_waitingline;




    private Behaviour_Server behaviour_server;


    public Behaviour_QueuePlace(
    ) {
        super(
        );
    }



    public Behaviour_WaitingLine getBehaviour_waitingline() {
        return behaviour_waitingline;
    }

    public void setBehaviour_waitingline(Behaviour_WaitingLine behaviour_waitingline) {
        this.behaviour_waitingline = behaviour_waitingline;
    }
    public Behaviour_Server getBehaviour_server() {
        return behaviour_server;
    }

    public void setBehaviour_server(Behaviour_Server behaviour_server) {
        this.behaviour_server = behaviour_server;
    }

}