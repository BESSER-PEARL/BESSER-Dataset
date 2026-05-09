





import java.util.List;
import java.util.ArrayList;

public class project_TaskAttributes extends ExportAttribute {

    private boolean none;
    private boolean note;
    private boolean complete;
    private boolean all;
    private boolean minend;
    private boolean booking;
    private boolean responsible;
    private boolean minstart;
    private boolean flags;
    private boolean depends;
    private boolean maxend;
    private boolean priority;
    private boolean maxstart;



    public project_TaskAttributes(
        boolean none,        boolean note,        boolean complete,        boolean all,        boolean minend,        boolean booking,        boolean responsible,        boolean minstart,        boolean flags,        boolean depends,        boolean maxend,        boolean priority,        boolean maxstart    ) {
        super(
        );
        this.none = none;
        this.note = note;
        this.complete = complete;
        this.all = all;
        this.minend = minend;
        this.booking = booking;
        this.responsible = responsible;
        this.minstart = minstart;
        this.flags = flags;
        this.depends = depends;
        this.maxend = maxend;
        this.priority = priority;
        this.maxstart = maxstart;
    }


    public boolean getNone() {
        return none;
    }

    public void setNone(boolean none) {
        this.none = none;
    }
    public boolean getNote() {
        return note;
    }

    public void setNote(boolean note) {
        this.note = note;
    }
    public boolean getComplete() {
        return complete;
    }

    public void setComplete(boolean complete) {
        this.complete = complete;
    }
    public boolean getAll() {
        return all;
    }

    public void setAll(boolean all) {
        this.all = all;
    }
    public boolean getMinend() {
        return minend;
    }

    public void setMinend(boolean minend) {
        this.minend = minend;
    }
    public boolean getBooking() {
        return booking;
    }

    public void setBooking(boolean booking) {
        this.booking = booking;
    }
    public boolean getResponsible() {
        return responsible;
    }

    public void setResponsible(boolean responsible) {
        this.responsible = responsible;
    }
    public boolean getMinstart() {
        return minstart;
    }

    public void setMinstart(boolean minstart) {
        this.minstart = minstart;
    }
    public boolean getFlags() {
        return flags;
    }

    public void setFlags(boolean flags) {
        this.flags = flags;
    }
    public boolean getDepends() {
        return depends;
    }

    public void setDepends(boolean depends) {
        this.depends = depends;
    }
    public boolean getMaxend() {
        return maxend;
    }

    public void setMaxend(boolean maxend) {
        this.maxend = maxend;
    }
    public boolean getPriority() {
        return priority;
    }

    public void setPriority(boolean priority) {
        this.priority = priority;
    }
    public boolean getMaxstart() {
        return maxstart;
    }

    public void setMaxstart(boolean maxstart) {
        this.maxstart = maxstart;
    }


}