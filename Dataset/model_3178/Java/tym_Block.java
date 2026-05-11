





import java.util.List;
import java.util.ArrayList;

public class tym_Block  {






    private List<tym_AbstractElement> tym_abstractelements;




    private tym_TestStatement tym_teststatement;




    private tym_LoopStatement tym_loopstatement;




    private tym_TestStatement tym_teststatement;


    public tym_Block(
    ) {
        this.tym_abstractelements = new ArrayList<>();
    }

    public tym_Block(
        ArrayList<tym_AbstractElement> tym_abstractelements    ) {
        this.tym_abstractelements = tym_abstractelements;
    }


    public List<tym_AbstractElement> getTym_abstractelements() {
        return tym_abstractelements;
    }

    public void addTym_abstractelement(Tym_abstractelement tym_abstractelement) {
        this.tym_abstractelements.add(tym_abstractelement);
    }
    public tym_TestStatement getTym_teststatement() {
        return tym_teststatement;
    }

    public void setTym_teststatement(tym_TestStatement tym_teststatement) {
        this.tym_teststatement = tym_teststatement;
    }
    public tym_LoopStatement getTym_loopstatement() {
        return tym_loopstatement;
    }

    public void setTym_loopstatement(tym_LoopStatement tym_loopstatement) {
        this.tym_loopstatement = tym_loopstatement;
    }
    public tym_TestStatement getTym_teststatement() {
        return tym_teststatement;
    }

    public void setTym_teststatement(tym_TestStatement tym_teststatement) {
        this.tym_teststatement = tym_teststatement;
    }

}