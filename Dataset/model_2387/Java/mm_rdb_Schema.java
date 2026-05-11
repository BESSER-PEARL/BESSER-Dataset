





import java.util.List;
import java.util.ArrayList;

public class mm_rdb_Schema  {

    private String name;





    private List<Index> indexs;


    public mm_rdb_Schema(
        String name    ) {
        this.name = name;
        this.indexs = new ArrayList<>();
    }

    public mm_rdb_Schema(
        String name        ArrayList<Index> indexs    ) {
        this.name = name;
        this.indexs = indexs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Index> getIndexs() {
        return indexs;
    }

    public void addIndex(Index index) {
        this.indexs.add(index);
    }

}