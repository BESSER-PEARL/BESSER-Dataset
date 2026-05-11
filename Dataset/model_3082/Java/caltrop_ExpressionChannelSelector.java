





import java.util.List;
import java.util.ArrayList;

public class caltrop_ExpressionChannelSelector extends ChannelSelector {

    private boolean many;



    public caltrop_ExpressionChannelSelector(
        boolean many    ) {
        super(
        );
        this.many = many;
    }


    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }


}