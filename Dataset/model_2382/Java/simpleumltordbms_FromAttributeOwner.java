





import java.util.List;
import java.util.ArrayList;

public class simpleumltordbms_FromAttributeOwner  {






    private simpleumltordbms_FromAttribute simpleumltordbms_fromattribute;




    private List<simpleumltordbms_FromAttribute> simpleumltordbms_fromattributes;


    public simpleumltordbms_FromAttributeOwner(
    ) {
        this.simpleumltordbms_fromattributes = new ArrayList<>();
    }

    public simpleumltordbms_FromAttributeOwner(
        ArrayList<simpleumltordbms_FromAttribute> simpleumltordbms_fromattributes    ) {
        this.simpleumltordbms_fromattributes = simpleumltordbms_fromattributes;
    }


    public simpleumltordbms_FromAttribute getSimpleumltordbms_fromattribute() {
        return simpleumltordbms_fromattribute;
    }

    public void setSimpleumltordbms_fromattribute(simpleumltordbms_FromAttribute simpleumltordbms_fromattribute) {
        this.simpleumltordbms_fromattribute = simpleumltordbms_fromattribute;
    }
    public List<simpleumltordbms_FromAttribute> getSimpleumltordbms_fromattributes() {
        return simpleumltordbms_fromattributes;
    }

    public void addSimpleumltordbms_fromattribute(Simpleumltordbms_fromattribute simpleumltordbms_fromattribute) {
        this.simpleumltordbms_fromattributes.add(simpleumltordbms_fromattribute);
    }

}