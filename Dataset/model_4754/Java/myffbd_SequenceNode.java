





import java.util.List;
import java.util.ArrayList;

public class myffbd_SequenceNode  {

    private String name;





    private myffbd_Function myffbd_function;




    private myffbd_SequenceNode myffbd_sequencenode;


    public myffbd_SequenceNode(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myffbd_Function getMyffbd_function() {
        return myffbd_function;
    }

    public void setMyffbd_function(myffbd_Function myffbd_function) {
        this.myffbd_function = myffbd_function;
    }
    public myffbd_SequenceNode getMyffbd_sequencenode() {
        return myffbd_sequencenode;
    }

    public void setMyffbd_sequencenode(myffbd_SequenceNode myffbd_sequencenode) {
        this.myffbd_sequencenode = myffbd_sequencenode;
    }

}