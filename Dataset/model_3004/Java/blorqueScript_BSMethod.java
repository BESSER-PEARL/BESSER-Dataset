





import java.util.List;
import java.util.ArrayList;

public class blorqueScript_BSMethod extends BSMember {






    private blorqueScript_BSMethodBody blorquescript_bsmethodbody;




    private List<blorqueScript_BSParameter> blorquescript_bsparameters;


    public blorqueScript_BSMethod(
    ) {
        super(
        );
        this.blorquescript_bsparameters = new ArrayList<>();
    }

    public blorqueScript_BSMethod(
        ArrayList<blorqueScript_BSParameter> blorquescript_bsparameters    ) {
        this.blorquescript_bsparameters = blorquescript_bsparameters;
    }


    public blorqueScript_BSMethodBody getBlorquescript_bsmethodbody() {
        return blorquescript_bsmethodbody;
    }

    public void setBlorquescript_bsmethodbody(blorqueScript_BSMethodBody blorquescript_bsmethodbody) {
        this.blorquescript_bsmethodbody = blorquescript_bsmethodbody;
    }
    public List<blorqueScript_BSParameter> getBlorquescript_bsparameters() {
        return blorquescript_bsparameters;
    }

    public void addBlorquescript_bsparameter(Blorquescript_bsparameter blorquescript_bsparameter) {
        this.blorquescript_bsparameters.add(blorquescript_bsparameter);
    }

}