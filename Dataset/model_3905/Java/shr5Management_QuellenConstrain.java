





import java.util.List;
import java.util.ArrayList;

public class shr5Management_QuellenConstrain  {

    private String constrainType;





    private List<shr5Management_Quelle> shr5management_quelles;




    private shr5Management_CharacterGeneratorSystem shr5management_charactergeneratorsystem;




    private shr5Management_Quelle shr5management_quelle;


    public shr5Management_QuellenConstrain(
        String constrainType    ) {
        this.constrainType = constrainType;
        this.shr5management_quelles = new ArrayList<>();
    }

    public shr5Management_QuellenConstrain(
        String constrainType        ArrayList<shr5Management_Quelle> shr5management_quelles    ) {
        this.constrainType = constrainType;
        this.shr5management_quelles = shr5management_quelles;
    }

    public String getConstraintype() {
        return constrainType;
    }

    public void setConstraintype(String constrainType) {
        this.constrainType = constrainType;
    }

    public List<shr5Management_Quelle> getShr5management_quelles() {
        return shr5management_quelles;
    }

    public void addShr5management_quelle(Shr5management_quelle shr5management_quelle) {
        this.shr5management_quelles.add(shr5management_quelle);
    }
    public shr5Management_CharacterGeneratorSystem getShr5management_charactergeneratorsystem() {
        return shr5management_charactergeneratorsystem;
    }

    public void setShr5management_charactergeneratorsystem(shr5Management_CharacterGeneratorSystem shr5management_charactergeneratorsystem) {
        this.shr5management_charactergeneratorsystem = shr5management_charactergeneratorsystem;
    }
    public shr5Management_Quelle getShr5management_quelle() {
        return shr5management_quelle;
    }

    public void setShr5management_quelle(shr5Management_Quelle shr5management_quelle) {
        this.shr5management_quelle = shr5management_quelle;
    }

}