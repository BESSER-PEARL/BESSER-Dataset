





import java.util.List;
import java.util.ArrayList;

public class xwiki_HistoryType extends LinkCollection {






    private List<xwiki_HistorySummary> xwiki_historysummarys;


    public xwiki_HistoryType(
    ) {
        super(
        );
        this.xwiki_historysummarys = new ArrayList<>();
    }

    public xwiki_HistoryType(
        ArrayList<xwiki_HistorySummary> xwiki_historysummarys    ) {
        this.xwiki_historysummarys = xwiki_historysummarys;
    }


    public List<xwiki_HistorySummary> getXwiki_historysummarys() {
        return xwiki_historysummarys;
    }

    public void addXwiki_historysummary(Xwiki_historysummary xwiki_historysummary) {
        this.xwiki_historysummarys.add(xwiki_historysummary);
    }

}