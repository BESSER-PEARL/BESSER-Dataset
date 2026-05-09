





import java.util.List;
import java.util.ArrayList;

public class project_JournalAttributes extends ReportAttribute {

    private boolean none;
    private boolean propertyid;
    private boolean all;
    private boolean author;
    private boolean _property;
    private boolean flags;
    private boolean timesheet;
    private boolean details;
    private boolean headline;
    private boolean date;
    private boolean summary;



    public project_JournalAttributes(
        boolean none,        boolean propertyid,        boolean all,        boolean author,        boolean _property,        boolean flags,        boolean timesheet,        boolean details,        boolean headline,        boolean date,        boolean summary    ) {
        super(
        );
        this.none = none;
        this.propertyid = propertyid;
        this.all = all;
        this.author = author;
        this._property = _property;
        this.flags = flags;
        this.timesheet = timesheet;
        this.details = details;
        this.headline = headline;
        this.date = date;
        this.summary = summary;
    }


    public boolean getNone() {
        return none;
    }

    public void setNone(boolean none) {
        this.none = none;
    }
    public boolean getPropertyid() {
        return propertyid;
    }

    public void setPropertyid(boolean propertyid) {
        this.propertyid = propertyid;
    }
    public boolean getAll() {
        return all;
    }

    public void setAll(boolean all) {
        this.all = all;
    }
    public boolean getAuthor() {
        return author;
    }

    public void setAuthor(boolean author) {
        this.author = author;
    }
    public boolean get_property() {
        return _property;
    }

    public void set_property(boolean _property) {
        this._property = _property;
    }
    public boolean getFlags() {
        return flags;
    }

    public void setFlags(boolean flags) {
        this.flags = flags;
    }
    public boolean getTimesheet() {
        return timesheet;
    }

    public void setTimesheet(boolean timesheet) {
        this.timesheet = timesheet;
    }
    public boolean getDetails() {
        return details;
    }

    public void setDetails(boolean details) {
        this.details = details;
    }
    public boolean getHeadline() {
        return headline;
    }

    public void setHeadline(boolean headline) {
        this.headline = headline;
    }
    public boolean getDate() {
        return date;
    }

    public void setDate(boolean date) {
        this.date = date;
    }
    public boolean getSummary() {
        return summary;
    }

    public void setSummary(boolean summary) {
        this.summary = summary;
    }


}