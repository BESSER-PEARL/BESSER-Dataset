





import java.util.List;
import java.util.ArrayList;

public class library_Library  {

    private String options;
    private String name;
    private String writerByIDMap;



    public library_Library(
        String options,        String name,        String writerByIDMap    ) {
        this.options = options;
        this.name = name;
        this.writerByIDMap = writerByIDMap;
    }


    public String getOptions() {
        return options;
    }

    public void setOptions(String options) {
        this.options = options;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getWriterbyidmap() {
        return writerByIDMap;
    }

    public void setWriterbyidmap(String writerByIDMap) {
        this.writerByIDMap = writerByIDMap;
    }


}