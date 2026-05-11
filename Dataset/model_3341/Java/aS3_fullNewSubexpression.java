





import java.util.List;
import java.util.ArrayList;

public class aS3_fullNewSubexpression  {

    private String fnsd;





    private List<aS3_primaryExpression> as3_primaryexpressions;




    private List<aS3_brackets> as3_bracketss;




    private List<aS3_qualifiedIdent> as3_qualifiedidents;


    public aS3_fullNewSubexpression(
        String fnsd    ) {
        this.fnsd = fnsd;
        this.as3_primaryexpressions = new ArrayList<>();
        this.as3_bracketss = new ArrayList<>();
        this.as3_qualifiedidents = new ArrayList<>();
    }

    public aS3_fullNewSubexpression(
        String fnsd        ArrayList<aS3_primaryExpression> as3_primaryexpressions,        ArrayList<aS3_brackets> as3_bracketss,        ArrayList<aS3_qualifiedIdent> as3_qualifiedidents    ) {
        this.fnsd = fnsd;
        this.as3_primaryexpressions = as3_primaryexpressions;
        this.as3_bracketss = as3_bracketss;
        this.as3_qualifiedidents = as3_qualifiedidents;
    }

    public String getFnsd() {
        return fnsd;
    }

    public void setFnsd(String fnsd) {
        this.fnsd = fnsd;
    }

    public List<aS3_primaryExpression> getAs3_primaryexpressions() {
        return as3_primaryexpressions;
    }

    public void addAs3_primaryexpression(As3_primaryexpression as3_primaryexpression) {
        this.as3_primaryexpressions.add(as3_primaryexpression);
    }
    public List<aS3_brackets> getAs3_bracketss() {
        return as3_bracketss;
    }

    public void addAs3_brackets(As3_brackets as3_brackets) {
        this.as3_bracketss.add(as3_brackets);
    }
    public List<aS3_qualifiedIdent> getAs3_qualifiedidents() {
        return as3_qualifiedidents;
    }

    public void addAs3_qualifiedident(As3_qualifiedident as3_qualifiedident) {
        this.as3_qualifiedidents.add(as3_qualifiedident);
    }

}