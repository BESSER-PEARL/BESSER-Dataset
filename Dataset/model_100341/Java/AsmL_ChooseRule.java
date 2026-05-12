





import java.util.List;
import java.util.ArrayList;

public class AsmL_ChooseRule extends Rule {






    private Body body;




    private List<InWhereHolds> inwhereholdss;




    private Body body;


    public AsmL_ChooseRule(
    ) {
        super(
        );
        this.inwhereholdss = new ArrayList<>();
    }

    public AsmL_ChooseRule(
        ArrayList<InWhereHolds> inwhereholdss    ) {
        this.inwhereholdss = inwhereholdss;
    }


    public Body getBody() {
        return body;
    }

    public void setBody(Body body) {
        this.body = body;
    }
    public List<InWhereHolds> getInwhereholdss() {
        return inwhereholdss;
    }

    public void addInwhereholds(Inwhereholds inwhereholds) {
        this.inwhereholdss.add(inwhereholds);
    }
    public Body getBody() {
        return body;
    }

    public void setBody(Body body) {
        this.body = body;
    }

}