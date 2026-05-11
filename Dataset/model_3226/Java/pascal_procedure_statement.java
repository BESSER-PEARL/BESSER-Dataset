





import java.util.List;
import java.util.ArrayList;

public class pascal_procedure_statement extends simple_statement {

    private String actualParameterList;
    private String name;



    public pascal_procedure_statement(
        String actualParameterList,        String name    ) {
        super(
        );
        this.actualParameterList = actualParameterList;
        this.name = name;
    }


    public String getActualparameterlist() {
        return actualParameterList;
    }

    public void setActualparameterlist(String actualParameterList) {
        this.actualParameterList = actualParameterList;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}