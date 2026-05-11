





import java.util.List;
import java.util.ArrayList;

public class myDsl_Array_initializer  {






    private List<myDsl_Variable_initializer> mydsl_variable_initializers;




    private myDsl_Variable_initializer mydsl_variable_initializer;


    public myDsl_Array_initializer(
    ) {
        this.mydsl_variable_initializers = new ArrayList<>();
    }

    public myDsl_Array_initializer(
        ArrayList<myDsl_Variable_initializer> mydsl_variable_initializers    ) {
        this.mydsl_variable_initializers = mydsl_variable_initializers;
    }


    public List<myDsl_Variable_initializer> getMydsl_variable_initializers() {
        return mydsl_variable_initializers;
    }

    public void addMydsl_variable_initializer(Mydsl_variable_initializer mydsl_variable_initializer) {
        this.mydsl_variable_initializers.add(mydsl_variable_initializer);
    }
    public myDsl_Variable_initializer getMydsl_variable_initializer() {
        return mydsl_variable_initializer;
    }

    public void setMydsl_variable_initializer(myDsl_Variable_initializer mydsl_variable_initializer) {
        this.mydsl_variable_initializer = mydsl_variable_initializer;
    }

}