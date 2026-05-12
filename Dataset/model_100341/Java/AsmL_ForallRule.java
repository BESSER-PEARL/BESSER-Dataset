





import java.util.List;
import java.util.ArrayList;

public class AsmL_ForallRule extends Rule {






    private Body body;




    private List<InWhereHolds> inwhereholdss;


    public AsmL_ForallRule(
    ) {
        super(
        );
        this.inwhereholdss = new ArrayList<>();
    }

    public AsmL_ForallRule(
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

}