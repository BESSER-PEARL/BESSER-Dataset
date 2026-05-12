





import java.util.List;
import java.util.ArrayList;

public class sourcecleaner_Plugin extends Source {

    private String extra;



    public sourcecleaner_Plugin(
        String extra    ) {
        super(
        );
        this.extra = extra;
    }


    public String getExtra() {
        return extra;
    }

    public void setExtra(String extra) {
        this.extra = extra;
    }


}