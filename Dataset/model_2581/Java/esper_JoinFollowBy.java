





import java.util.List;
import java.util.ArrayList;

public class esper_JoinFollowBy  {

    private String operator;





    private esper_Pattern esper_pattern;




    private List<esper_AbstractFollowBy> esper_abstractfollowbys;


    public esper_JoinFollowBy(
        String operator    ) {
        this.operator = operator;
        this.esper_abstractfollowbys = new ArrayList<>();
    }

    public esper_JoinFollowBy(
        String operator        ArrayList<esper_AbstractFollowBy> esper_abstractfollowbys    ) {
        this.operator = operator;
        this.esper_abstractfollowbys = esper_abstractfollowbys;
    }

    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public esper_Pattern getEsper_pattern() {
        return esper_pattern;
    }

    public void setEsper_pattern(esper_Pattern esper_pattern) {
        this.esper_pattern = esper_pattern;
    }
    public List<esper_AbstractFollowBy> getEsper_abstractfollowbys() {
        return esper_abstractfollowbys;
    }

    public void addEsper_abstractfollowby(Esper_abstractfollowby esper_abstractfollowby) {
        this.esper_abstractfollowbys.add(esper_abstractfollowby);
    }

}