





import java.util.List;
import java.util.ArrayList;

public class sample_Type  {

    private String name;





    private sample_TypeMap sample_typemap;


    public sample_Type(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sample_TypeMap getSample_typemap() {
        return sample_typemap;
    }

    public void setSample_typemap(sample_TypeMap sample_typemap) {
        this.sample_typemap = sample_typemap;
    }

}