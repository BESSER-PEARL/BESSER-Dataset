





import java.util.List;
import java.util.ArrayList;

public class minilang_Variable  {

    private String name;
    private float value;





    private minilang_Program minilang_program;


    public minilang_Variable(
        String name,        float value    ) {
        this.name = name;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }

    public minilang_Program getMinilang_program() {
        return minilang_program;
    }

    public void setMinilang_program(minilang_Program minilang_program) {
        this.minilang_program = minilang_program;
    }

}