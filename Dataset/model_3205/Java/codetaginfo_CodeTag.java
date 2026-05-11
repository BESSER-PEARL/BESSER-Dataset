





import java.util.List;
import java.util.ArrayList;

public class codetaginfo_CodeTag  {

    private String contents;
    private String group;
    private String type;
    private String tag_end;
    private String uuid;
    private String tag_begin;
    private String name;



    public codetaginfo_CodeTag(
        String contents,        String group,        String type,        String tag_end,        String uuid,        String tag_begin,        String name    ) {
        this.contents = contents;
        this.group = group;
        this.type = type;
        this.tag_end = tag_end;
        this.uuid = uuid;
        this.tag_begin = tag_begin;
        this.name = name;
    }


    public String getContents() {
        return contents;
    }

    public void setContents(String contents) {
        this.contents = contents;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getTag_end() {
        return tag_end;
    }

    public void setTag_end(String tag_end) {
        this.tag_end = tag_end;
    }
    public String getUuid() {
        return uuid;
    }

    public void setUuid(String uuid) {
        this.uuid = uuid;
    }
    public String getTag_begin() {
        return tag_begin;
    }

    public void setTag_begin(String tag_begin) {
        this.tag_begin = tag_begin;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}