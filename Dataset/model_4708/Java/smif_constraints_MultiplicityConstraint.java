





import java.util.List;
import java.util.ArrayList;

public class smif_constraints_MultiplicityConstraint extends TypeConstraint {

    private String mininumNumber;
    private String maximumNumber;
    private String atOnce;
    private String isSufficent;





    private Type type;




    private List<Type> types;


    public smif_constraints_MultiplicityConstraint(
        String mininumNumber,        String maximumNumber,        String atOnce,        String isSufficent    ) {
        super(
        );
        this.mininumNumber = mininumNumber;
        this.maximumNumber = maximumNumber;
        this.atOnce = atOnce;
        this.isSufficent = isSufficent;
        this.types = new ArrayList<>();
    }

    public smif_constraints_MultiplicityConstraint(
        String mininumNumber,        String maximumNumber,        String atOnce,        String isSufficent        ArrayList<Type> types    ) {
        this.mininumNumber = mininumNumber;
        this.maximumNumber = maximumNumber;
        this.atOnce = atOnce;
        this.isSufficent = isSufficent;
        this.types = types;
    }

    public String getMininumnumber() {
        return mininumNumber;
    }

    public void setMininumnumber(String mininumNumber) {
        this.mininumNumber = mininumNumber;
    }
    public String getMaximumnumber() {
        return maximumNumber;
    }

    public void setMaximumnumber(String maximumNumber) {
        this.maximumNumber = maximumNumber;
    }
    public String getAtonce() {
        return atOnce;
    }

    public void setAtonce(String atOnce) {
        this.atOnce = atOnce;
    }
    public String getIssufficent() {
        return isSufficent;
    }

    public void setIssufficent(String isSufficent) {
        this.isSufficent = isSufficent;
    }

    public Type getType() {
        return type;
    }

    public void setType(Type type) {
        this.type = type;
    }
    public List<Type> getTypes() {
        return types;
    }

    public void addType(Type type) {
        this.types.add(type);
    }

}