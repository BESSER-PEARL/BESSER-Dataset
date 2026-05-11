





import java.util.List;
import java.util.ArrayList;

public class becontent_Handler extends BeContentElement {

    private boolean mainSkinWithPager;
    private int mainSkinPagerLength;
    private String fileName;
    private String mainSkinPlaceholder;



    public becontent_Handler(
        boolean mainSkinWithPager,        int mainSkinPagerLength,        String fileName,        String mainSkinPlaceholder    ) {
        super(
        );
        this.mainSkinWithPager = mainSkinWithPager;
        this.mainSkinPagerLength = mainSkinPagerLength;
        this.fileName = fileName;
        this.mainSkinPlaceholder = mainSkinPlaceholder;
    }


    public boolean getMainskinwithpager() {
        return mainSkinWithPager;
    }

    public void setMainskinwithpager(boolean mainSkinWithPager) {
        this.mainSkinWithPager = mainSkinWithPager;
    }
    public int getMainskinpagerlength() {
        return mainSkinPagerLength;
    }

    public void setMainskinpagerlength(int mainSkinPagerLength) {
        this.mainSkinPagerLength = mainSkinPagerLength;
    }
    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }
    public String getMainskinplaceholder() {
        return mainSkinPlaceholder;
    }

    public void setMainskinplaceholder(String mainSkinPlaceholder) {
        this.mainSkinPlaceholder = mainSkinPlaceholder;
    }


}