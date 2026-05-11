





import java.util.List;
import java.util.ArrayList;

public class pascal_scale_factor  {

    private String sign;





    private pascal_real_number pascal_real_number;




    private pascal_digit_sequence pascal_digit_sequence;


    public pascal_scale_factor(
        String sign    ) {
        this.sign = sign;
    }


    public String getSign() {
        return sign;
    }

    public void setSign(String sign) {
        this.sign = sign;
    }

    public pascal_real_number getPascal_real_number() {
        return pascal_real_number;
    }

    public void setPascal_real_number(pascal_real_number pascal_real_number) {
        this.pascal_real_number = pascal_real_number;
    }
    public pascal_digit_sequence getPascal_digit_sequence() {
        return pascal_digit_sequence;
    }

    public void setPascal_digit_sequence(pascal_digit_sequence pascal_digit_sequence) {
        this.pascal_digit_sequence = pascal_digit_sequence;
    }

}