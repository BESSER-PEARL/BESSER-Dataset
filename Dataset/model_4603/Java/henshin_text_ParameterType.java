





import java.util.List;
import java.util.ArrayList;

public class henshin_text_ParameterType  {

    private String enumType;





    private henshin_text_Parameter henshin_text_parameter;




    private henshin_text_EClass henshin_text_eclass;


    public henshin_text_ParameterType(
        String enumType    ) {
        this.enumType = enumType;
    }


    public String getEnumtype() {
        return enumType;
    }

    public void setEnumtype(String enumType) {
        this.enumType = enumType;
    }

    public henshin_text_Parameter getHenshin_text_parameter() {
        return henshin_text_parameter;
    }

    public void setHenshin_text_parameter(henshin_text_Parameter henshin_text_parameter) {
        this.henshin_text_parameter = henshin_text_parameter;
    }
    public henshin_text_EClass getHenshin_text_eclass() {
        return henshin_text_eclass;
    }

    public void setHenshin_text_eclass(henshin_text_EClass henshin_text_eclass) {
        this.henshin_text_eclass = henshin_text_eclass;
    }

}