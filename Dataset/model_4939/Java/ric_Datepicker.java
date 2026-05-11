





import java.util.List;
import java.util.ArrayList;

public class ric_Datepicker extends TextField, RichWidget {

    private boolean showWeekOfYear;
    private boolean showButtonImage;
    private boolean showYearMenu;
    private String dateFormat;
    private boolean showMonthMenu;
    private int numberMonthsToShow;
    private boolean showButtonClosePanel;
    private String locale;



    public ric_Datepicker(
        boolean showWeekOfYear,        boolean showButtonImage,        boolean showYearMenu,        String dateFormat,        boolean showMonthMenu,        int numberMonthsToShow,        boolean showButtonClosePanel,        String locale    ) {
        super(
        );
        this.showWeekOfYear = showWeekOfYear;
        this.showButtonImage = showButtonImage;
        this.showYearMenu = showYearMenu;
        this.dateFormat = dateFormat;
        this.showMonthMenu = showMonthMenu;
        this.numberMonthsToShow = numberMonthsToShow;
        this.showButtonClosePanel = showButtonClosePanel;
        this.locale = locale;
    }


    public boolean getShowweekofyear() {
        return showWeekOfYear;
    }

    public void setShowweekofyear(boolean showWeekOfYear) {
        this.showWeekOfYear = showWeekOfYear;
    }
    public boolean getShowbuttonimage() {
        return showButtonImage;
    }

    public void setShowbuttonimage(boolean showButtonImage) {
        this.showButtonImage = showButtonImage;
    }
    public boolean getShowyearmenu() {
        return showYearMenu;
    }

    public void setShowyearmenu(boolean showYearMenu) {
        this.showYearMenu = showYearMenu;
    }
    public String getDateformat() {
        return dateFormat;
    }

    public void setDateformat(String dateFormat) {
        this.dateFormat = dateFormat;
    }
    public boolean getShowmonthmenu() {
        return showMonthMenu;
    }

    public void setShowmonthmenu(boolean showMonthMenu) {
        this.showMonthMenu = showMonthMenu;
    }
    public int getNumbermonthstoshow() {
        return numberMonthsToShow;
    }

    public void setNumbermonthstoshow(int numberMonthsToShow) {
        this.numberMonthsToShow = numberMonthsToShow;
    }
    public boolean getShowbuttonclosepanel() {
        return showButtonClosePanel;
    }

    public void setShowbuttonclosepanel(boolean showButtonClosePanel) {
        this.showButtonClosePanel = showButtonClosePanel;
    }
    public String getLocale() {
        return locale;
    }

    public void setLocale(String locale) {
        this.locale = locale;
    }


}