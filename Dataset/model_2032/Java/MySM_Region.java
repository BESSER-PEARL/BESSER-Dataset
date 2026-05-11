





import java.util.List;
import java.util.ArrayList;

public class MySM_Region  {

    private String name;





    private MySM_ComplexSate mysm_complexsate;


    public MySM_Region(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public MySM_ComplexSate getMysm_complexsate() {
        return mysm_complexsate;
    }

    public void setMysm_complexsate(MySM_ComplexSate mysm_complexsate) {
        this.mysm_complexsate = mysm_complexsate;
    }

}