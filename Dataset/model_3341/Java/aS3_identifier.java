





import java.util.List;
import java.util.ArrayList;

public class aS3_identifier  {






    private aS3_qualifiedIdent as3_qualifiedident;




    private List<aS3_propOrIdent> as3_proporidents;


    public aS3_identifier(
    ) {
        this.as3_proporidents = new ArrayList<>();
    }

    public aS3_identifier(
        ArrayList<aS3_propOrIdent> as3_proporidents    ) {
        this.as3_proporidents = as3_proporidents;
    }


    public aS3_qualifiedIdent getAs3_qualifiedident() {
        return as3_qualifiedident;
    }

    public void setAs3_qualifiedident(aS3_qualifiedIdent as3_qualifiedident) {
        this.as3_qualifiedident = as3_qualifiedident;
    }
    public List<aS3_propOrIdent> getAs3_proporidents() {
        return as3_proporidents;
    }

    public void addAs3_proporident(As3_proporident as3_proporident) {
        this.as3_proporidents.add(as3_proporident);
    }

}