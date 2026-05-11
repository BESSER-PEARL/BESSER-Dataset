





import java.util.List;
import java.util.ArrayList;

public class myfsm_State  {

    private String name;





    private myfsm_Machine myfsm_machine;




    private myfsm_Machine myfsm_machine;




    private myfsm_Trans myfsm_trans;




    private List<myfsm_Trans> myfsm_transs;


    public myfsm_State(
        String name    ) {
        this.name = name;
        this.myfsm_transs = new ArrayList<>();
    }

    public myfsm_State(
        String name        ArrayList<myfsm_Trans> myfsm_transs    ) {
        this.name = name;
        this.myfsm_transs = myfsm_transs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myfsm_Machine getMyfsm_machine() {
        return myfsm_machine;
    }

    public void setMyfsm_machine(myfsm_Machine myfsm_machine) {
        this.myfsm_machine = myfsm_machine;
    }
    public myfsm_Machine getMyfsm_machine() {
        return myfsm_machine;
    }

    public void setMyfsm_machine(myfsm_Machine myfsm_machine) {
        this.myfsm_machine = myfsm_machine;
    }
    public myfsm_Trans getMyfsm_trans() {
        return myfsm_trans;
    }

    public void setMyfsm_trans(myfsm_Trans myfsm_trans) {
        this.myfsm_trans = myfsm_trans;
    }
    public List<myfsm_Trans> getMyfsm_transs() {
        return myfsm_transs;
    }

    public void addMyfsm_trans(Myfsm_trans myfsm_trans) {
        this.myfsm_transs.add(myfsm_trans);
    }

}