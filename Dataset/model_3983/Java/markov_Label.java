





import java.util.List;
import java.util.ArrayList;

public class markov_Label  {

    private String value;
    private String key;





    private markov_State markov_state;


    public markov_Label(
        String value,        String key    ) {
        this.value = value;
        this.key = key;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public markov_State getMarkov_state() {
        return markov_state;
    }

    public void setMarkov_state(markov_State markov_state) {
        this.markov_state = markov_state;
    }

}