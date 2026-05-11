





import java.util.List;
import java.util.ArrayList;

public class operators_Marker  {

    private String description;
    private String kind;





    private operators_Function operators_function;




    private operators_Equipment operators_equipment;


    public operators_Marker(
        String description,        String kind    ) {
        this.description = description;
        this.kind = kind;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public operators_Function getOperators_function() {
        return operators_function;
    }

    public void setOperators_function(operators_Function operators_function) {
        this.operators_function = operators_function;
    }
    public operators_Equipment getOperators_equipment() {
        return operators_equipment;
    }

    public void setOperators_equipment(operators_Equipment operators_equipment) {
        this.operators_equipment = operators_equipment;
    }

}