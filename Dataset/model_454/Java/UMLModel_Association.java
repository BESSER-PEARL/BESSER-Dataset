





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Association extends Relationship, Classifier {

    private String memberEnd;
    private String endType;
    private String navigableOwnedEnd;
    private String isDerived;



    public UMLModel_Association(
        String memberEnd,        String endType,        String navigableOwnedEnd,        String isDerived    ) {
        super(
        );
        this.memberEnd = memberEnd;
        this.endType = endType;
        this.navigableOwnedEnd = navigableOwnedEnd;
        this.isDerived = isDerived;
    }


    public String getMemberend() {
        return memberEnd;
    }

    public void setMemberend(String memberEnd) {
        this.memberEnd = memberEnd;
    }
    public String getEndtype() {
        return endType;
    }

    public void setEndtype(String endType) {
        this.endType = endType;
    }
    public String getNavigableownedend() {
        return navigableOwnedEnd;
    }

    public void setNavigableownedend(String navigableOwnedEnd) {
        this.navigableOwnedEnd = navigableOwnedEnd;
    }
    public String getIsderived() {
        return isDerived;
    }

    public void setIsderived(String isDerived) {
        this.isDerived = isDerived;
    }


}