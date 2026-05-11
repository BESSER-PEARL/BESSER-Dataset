





import java.util.List;
import java.util.ArrayList;

public class ccore_TimeAttribute extends LongAttribute {

    private boolean initWithTheCurrentTime;



    public ccore_TimeAttribute(
        boolean initWithTheCurrentTime    ) {
        super(
        );
        this.initWithTheCurrentTime = initWithTheCurrentTime;
    }


    public boolean getInitwiththecurrenttime() {
        return initWithTheCurrentTime;
    }

    public void setInitwiththecurrenttime(boolean initWithTheCurrentTime) {
        this.initWithTheCurrentTime = initWithTheCurrentTime;
    }


}