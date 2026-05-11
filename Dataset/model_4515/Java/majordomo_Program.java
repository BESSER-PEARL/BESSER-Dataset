





import java.util.List;
import java.util.ArrayList;

public class majordomo_Program  {






    private List<majordomo_PreparedValue> majordomo_preparedvalues;




    private List<majordomo_PreparedStatement> majordomo_preparedstatements;




    private majordomo_PreparedValue majordomo_preparedvalue;




    private List<majordomo_Rule> majordomo_rules;




    private List<majordomo_PreparedActionSet> majordomo_preparedactionsets;




    private majordomo_Majordomo majordomo_majordomo;




    private majordomo_PreparedStatement majordomo_preparedstatement;




    private majordomo_PreparedActionSet majordomo_preparedactionset;


    public majordomo_Program(
    ) {
        this.majordomo_preparedvalues = new ArrayList<>();
        this.majordomo_preparedstatements = new ArrayList<>();
        this.majordomo_rules = new ArrayList<>();
        this.majordomo_preparedactionsets = new ArrayList<>();
    }

    public majordomo_Program(
        ArrayList<majordomo_PreparedValue> majordomo_preparedvalues,        ArrayList<majordomo_PreparedStatement> majordomo_preparedstatements,        ArrayList<majordomo_Rule> majordomo_rules,        ArrayList<majordomo_PreparedActionSet> majordomo_preparedactionsets    ) {
        this.majordomo_preparedvalues = majordomo_preparedvalues;
        this.majordomo_preparedstatements = majordomo_preparedstatements;
        this.majordomo_rules = majordomo_rules;
        this.majordomo_preparedactionsets = majordomo_preparedactionsets;
    }


    public List<majordomo_PreparedValue> getMajordomo_preparedvalues() {
        return majordomo_preparedvalues;
    }

    public void addMajordomo_preparedvalue(Majordomo_preparedvalue majordomo_preparedvalue) {
        this.majordomo_preparedvalues.add(majordomo_preparedvalue);
    }
    public List<majordomo_PreparedStatement> getMajordomo_preparedstatements() {
        return majordomo_preparedstatements;
    }

    public void addMajordomo_preparedstatement(Majordomo_preparedstatement majordomo_preparedstatement) {
        this.majordomo_preparedstatements.add(majordomo_preparedstatement);
    }
    public majordomo_PreparedValue getMajordomo_preparedvalue() {
        return majordomo_preparedvalue;
    }

    public void setMajordomo_preparedvalue(majordomo_PreparedValue majordomo_preparedvalue) {
        this.majordomo_preparedvalue = majordomo_preparedvalue;
    }
    public List<majordomo_Rule> getMajordomo_rules() {
        return majordomo_rules;
    }

    public void addMajordomo_rule(Majordomo_rule majordomo_rule) {
        this.majordomo_rules.add(majordomo_rule);
    }
    public List<majordomo_PreparedActionSet> getMajordomo_preparedactionsets() {
        return majordomo_preparedactionsets;
    }

    public void addMajordomo_preparedactionset(Majordomo_preparedactionset majordomo_preparedactionset) {
        this.majordomo_preparedactionsets.add(majordomo_preparedactionset);
    }
    public majordomo_Majordomo getMajordomo_majordomo() {
        return majordomo_majordomo;
    }

    public void setMajordomo_majordomo(majordomo_Majordomo majordomo_majordomo) {
        this.majordomo_majordomo = majordomo_majordomo;
    }
    public majordomo_PreparedStatement getMajordomo_preparedstatement() {
        return majordomo_preparedstatement;
    }

    public void setMajordomo_preparedstatement(majordomo_PreparedStatement majordomo_preparedstatement) {
        this.majordomo_preparedstatement = majordomo_preparedstatement;
    }
    public majordomo_PreparedActionSet getMajordomo_preparedactionset() {
        return majordomo_preparedactionset;
    }

    public void setMajordomo_preparedactionset(majordomo_PreparedActionSet majordomo_preparedactionset) {
        this.majordomo_preparedactionset = majordomo_preparedactionset;
    }

}