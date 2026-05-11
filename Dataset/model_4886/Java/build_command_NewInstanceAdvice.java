





import java.util.List;
import java.util.ArrayList;

public class build_command_NewInstanceAdvice extends AdviceGroup {

    private String clazz;



    public build_command_NewInstanceAdvice(
        String clazz    ) {
        super(
        );
        this.clazz = clazz;
    }


    public String getClazz() {
        return clazz;
    }

    public void setClazz(String clazz) {
        this.clazz = clazz;
    }


}