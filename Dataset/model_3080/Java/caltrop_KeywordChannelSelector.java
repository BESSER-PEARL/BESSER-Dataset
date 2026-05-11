





import java.util.List;
import java.util.ArrayList;

public class caltrop_KeywordChannelSelector extends ChannelSelector {

    private String keyword;



    public caltrop_KeywordChannelSelector(
        String keyword    ) {
        super(
        );
        this.keyword = keyword;
    }


    public String getKeyword() {
        return keyword;
    }

    public void setKeyword(String keyword) {
        this.keyword = keyword;
    }


}