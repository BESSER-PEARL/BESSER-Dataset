





import java.util.List;
import java.util.ArrayList;

public class SOS_adtmm_Variable  {

    private String name;





    private Sort sort;


    public SOS_adtmm_Variable(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Sort getSort() {
        return sort;
    }

    public void setSort(Sort sort) {
        this.sort = sort;
    }

}