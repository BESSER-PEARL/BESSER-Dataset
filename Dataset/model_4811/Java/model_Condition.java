





import java.util.List;
import java.util.ArrayList;

public class model_Condition extends Expression {






    private model_While model_while;




    private model_ElseIf model_elseif;




    private model_RepeatUntil model_repeatuntil;




    private model_Source model_source;




    private model_If model_if;




    private model_Targets model_targets;


    public model_Condition(
    ) {
        super(
        );
    }



    public model_While getModel_while() {
        return model_while;
    }

    public void setModel_while(model_While model_while) {
        this.model_while = model_while;
    }
    public model_ElseIf getModel_elseif() {
        return model_elseif;
    }

    public void setModel_elseif(model_ElseIf model_elseif) {
        this.model_elseif = model_elseif;
    }
    public model_RepeatUntil getModel_repeatuntil() {
        return model_repeatuntil;
    }

    public void setModel_repeatuntil(model_RepeatUntil model_repeatuntil) {
        this.model_repeatuntil = model_repeatuntil;
    }
    public model_Source getModel_source() {
        return model_source;
    }

    public void setModel_source(model_Source model_source) {
        this.model_source = model_source;
    }
    public model_If getModel_if() {
        return model_if;
    }

    public void setModel_if(model_If model_if) {
        this.model_if = model_if;
    }
    public model_Targets getModel_targets() {
        return model_targets;
    }

    public void setModel_targets(model_Targets model_targets) {
        this.model_targets = model_targets;
    }

}