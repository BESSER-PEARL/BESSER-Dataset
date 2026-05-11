





import java.util.List;
import java.util.ArrayList;

public class NQC_Expression extends Statement {






    private NQC_AssignmentStatement nqc_assignmentstatement;




    private NQC_UntilStatement nqc_untilstatement;




    private NQC_DoWhileStatement nqc_dowhilestatement;




    private NQC_ForStatement nqc_forstatement;




    private NQC_RepeatStatement nqc_repeatstatement;




    private NQC_WhileStatement nqc_whilestatement;




    private NQC_IfStatement nqc_ifstatement;




    private NQC_SwitchStatement nqc_switchstatement;


    public NQC_Expression(
    ) {
        super(
        );
    }



    public NQC_AssignmentStatement getNqc_assignmentstatement() {
        return nqc_assignmentstatement;
    }

    public void setNqc_assignmentstatement(NQC_AssignmentStatement nqc_assignmentstatement) {
        this.nqc_assignmentstatement = nqc_assignmentstatement;
    }
    public NQC_UntilStatement getNqc_untilstatement() {
        return nqc_untilstatement;
    }

    public void setNqc_untilstatement(NQC_UntilStatement nqc_untilstatement) {
        this.nqc_untilstatement = nqc_untilstatement;
    }
    public NQC_DoWhileStatement getNqc_dowhilestatement() {
        return nqc_dowhilestatement;
    }

    public void setNqc_dowhilestatement(NQC_DoWhileStatement nqc_dowhilestatement) {
        this.nqc_dowhilestatement = nqc_dowhilestatement;
    }
    public NQC_ForStatement getNqc_forstatement() {
        return nqc_forstatement;
    }

    public void setNqc_forstatement(NQC_ForStatement nqc_forstatement) {
        this.nqc_forstatement = nqc_forstatement;
    }
    public NQC_RepeatStatement getNqc_repeatstatement() {
        return nqc_repeatstatement;
    }

    public void setNqc_repeatstatement(NQC_RepeatStatement nqc_repeatstatement) {
        this.nqc_repeatstatement = nqc_repeatstatement;
    }
    public NQC_WhileStatement getNqc_whilestatement() {
        return nqc_whilestatement;
    }

    public void setNqc_whilestatement(NQC_WhileStatement nqc_whilestatement) {
        this.nqc_whilestatement = nqc_whilestatement;
    }
    public NQC_IfStatement getNqc_ifstatement() {
        return nqc_ifstatement;
    }

    public void setNqc_ifstatement(NQC_IfStatement nqc_ifstatement) {
        this.nqc_ifstatement = nqc_ifstatement;
    }
    public NQC_SwitchStatement getNqc_switchstatement() {
        return nqc_switchstatement;
    }

    public void setNqc_switchstatement(NQC_SwitchStatement nqc_switchstatement) {
        this.nqc_switchstatement = nqc_switchstatement;
    }

}