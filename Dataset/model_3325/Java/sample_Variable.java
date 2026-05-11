





import java.util.List;
import java.util.ArrayList;

public class sample_Variable  {

    private String Name;
    private String Value;
    private String Type;





    private sample_Sentence sample_sentence;


    public sample_Variable(
        String Name,        String Value,        String Type    ) {
        this.Name = Name;
        this.Value = Value;
        this.Type = Type;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getValue() {
        return Value;
    }

    public void setValue(String Value) {
        this.Value = Value;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }

    public sample_Sentence getSample_sentence() {
        return sample_sentence;
    }

    public void setSample_sentence(sample_Sentence sample_sentence) {
        this.sample_sentence = sample_sentence;
    }

}