





import java.util.List;
import java.util.ArrayList;

public class atem_SetLocale extends AbstractComponent, SectionElementType {

    private String dsl_SetLocale_V1;
    private String dsl_SetLocale_V2;



    public atem_SetLocale(
        String dsl_SetLocale_V1,        String dsl_SetLocale_V2    ) {
        super(
        );
        this.dsl_SetLocale_V1 = dsl_SetLocale_V1;
        this.dsl_SetLocale_V2 = dsl_SetLocale_V2;
    }


    public String getDsl_setlocale_v1() {
        return dsl_SetLocale_V1;
    }

    public void setDsl_setlocale_v1(String dsl_SetLocale_V1) {
        this.dsl_SetLocale_V1 = dsl_SetLocale_V1;
    }
    public String getDsl_setlocale_v2() {
        return dsl_SetLocale_V2;
    }

    public void setDsl_setlocale_v2(String dsl_SetLocale_V2) {
        this.dsl_SetLocale_V2 = dsl_SetLocale_V2;
    }


}