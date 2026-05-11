





import java.util.List;
import java.util.ArrayList;

public class netModel_EnumMember  {

    private String name;
    private boolean assignment;
    private int value;





    private netModel_EnumTypeLiteral netmodel_enumtypeliteral;


    public netModel_EnumMember(
        String name,        boolean assignment,        int value    ) {
        this.name = name;
        this.assignment = assignment;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getAssignment() {
        return assignment;
    }

    public void setAssignment(boolean assignment) {
        this.assignment = assignment;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public netModel_EnumTypeLiteral getNetmodel_enumtypeliteral() {
        return netmodel_enumtypeliteral;
    }

    public void setNetmodel_enumtypeliteral(netModel_EnumTypeLiteral netmodel_enumtypeliteral) {
        this.netmodel_enumtypeliteral = netmodel_enumtypeliteral;
    }

}