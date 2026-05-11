





import java.util.List;
import java.util.ArrayList;

public class ric_Datepicker extends RichWidget, TextField {

    private boolean showButtonClosePanel;
    private boolean showWeekOfYear;
    private String locale;
    private String dateFormat;
    private boolean showMonthMenu;
    private int numberMonthsToShow;
    private boolean showButtonImage;
    private boolean showYearMenu;



    public ric_Datepicker(
        boolean showButtonClosePanel,        boolean showWeekOfYear,        String locale,        String dateFormat,        boolean showMonthMenu,        int numberMonthsToShow,        boolean showButtonImage,        boolean showYearMenu    ) {
        super(
        );
        this.showButtonClosePanel = showButtonClosePanel;
        this.showWeekOfYear = showWeekOfYear;
        this.locale = locale;
        this.dateFormat = dateFormat;
        this.showMonthMenu = showMonthMenu;
        this.numberMonthsToShow = numberMonthsToShow;
        this.showButtonImage = showButtonImage;
        this.showYearMenu = showYearMenu;
    }


    public boolean getShowbuttonclosepanel() {
        return showButtonClosePanel;
    }

    public void setShowbuttonclosepanel(boolean showButtonClosePanel) {
        this.showButtonClosePanel = showButtonClosePanel;
    }
    public boolean getShowweekofyear() {
        return showWeekOfYear;
    }

    public void setShowweekofyear(boolean showWeekOfYear) {
        this.showWeekOfYear = showWeekOfYear;
    }
    public String getLocale() {
        return locale;
    }

    public void setLocale(String locale) {
        this.locale = locale;
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


}