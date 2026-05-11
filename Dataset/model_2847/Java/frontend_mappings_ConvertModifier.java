





import java.util.List;
import java.util.ArrayList;

public class frontend_mappings_ConvertModifier extends AttributeModifier {

    private String converter;



    public frontend_mappings_ConvertModifier(
        String converter    ) {
        super(
        );
        this.converter = converter;
    }


    public String getConverter() {
        return converter;
    }

    public void setConverter(String converter) {
        this.converter = converter;
    }


}