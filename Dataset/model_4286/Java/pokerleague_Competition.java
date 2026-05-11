




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class pokerleague_Competition extends DescribedEntity {

    private int defaultTournamentAnnouncementLead;
    private int defaultBuyIn;
    private LocalDate startDate;
    private LocalDate endDate;
    private int defaultMinPlayers;
    private String defaultTournamentInvitationContact;
    private int minimalAttendance;
    private int defaultTournamentInvitationClosure;
    private int defaultMaxPlayers;





    private List<pokerleague_Player> pokerleague_players;




    private pokerleague_PrizeMoneyRuleSet pokerleague_prizemoneyruleset;


    public pokerleague_Competition(
        int defaultTournamentAnnouncementLead,        int defaultBuyIn,        LocalDate startDate,        LocalDate endDate,        int defaultMinPlayers,        String defaultTournamentInvitationContact,        int minimalAttendance,        int defaultTournamentInvitationClosure,        int defaultMaxPlayers    ) {
        super(
        );
        this.defaultTournamentAnnouncementLead = defaultTournamentAnnouncementLead;
        this.defaultBuyIn = defaultBuyIn;
        this.startDate = startDate;
        this.endDate = endDate;
        this.defaultMinPlayers = defaultMinPlayers;
        this.defaultTournamentInvitationContact = defaultTournamentInvitationContact;
        this.minimalAttendance = minimalAttendance;
        this.defaultTournamentInvitationClosure = defaultTournamentInvitationClosure;
        this.defaultMaxPlayers = defaultMaxPlayers;
        this.pokerleague_players = new ArrayList<>();
    }

    public pokerleague_Competition(
        int defaultTournamentAnnouncementLead,        int defaultBuyIn,        LocalDate startDate,        LocalDate endDate,        int defaultMinPlayers,        String defaultTournamentInvitationContact,        int minimalAttendance,        int defaultTournamentInvitationClosure,        int defaultMaxPlayers        ArrayList<pokerleague_Player> pokerleague_players    ) {
        this.defaultTournamentAnnouncementLead = defaultTournamentAnnouncementLead;
        this.defaultBuyIn = defaultBuyIn;
        this.startDate = startDate;
        this.endDate = endDate;
        this.defaultMinPlayers = defaultMinPlayers;
        this.defaultTournamentInvitationContact = defaultTournamentInvitationContact;
        this.minimalAttendance = minimalAttendance;
        this.defaultTournamentInvitationClosure = defaultTournamentInvitationClosure;
        this.defaultMaxPlayers = defaultMaxPlayers;
        this.pokerleague_players = pokerleague_players;
    }

    public int getDefaulttournamentannouncementlead() {
        return defaultTournamentAnnouncementLead;
    }

    public void setDefaulttournamentannouncementlead(int defaultTournamentAnnouncementLead) {
        this.defaultTournamentAnnouncementLead = defaultTournamentAnnouncementLead;
    }
    public int getDefaultbuyin() {
        return defaultBuyIn;
    }

    public void setDefaultbuyin(int defaultBuyIn) {
        this.defaultBuyIn = defaultBuyIn;
    }
    public LocalDate getStartdate() {
        return startDate;
    }

    public void setStartdate(LocalDate startDate) {
        this.startDate = startDate;
    }
    public LocalDate getEnddate() {
        return endDate;
    }

    public void setEnddate(LocalDate endDate) {
        this.endDate = endDate;
    }
    public int getDefaultminplayers() {
        return defaultMinPlayers;
    }

    public void setDefaultminplayers(int defaultMinPlayers) {
        this.defaultMinPlayers = defaultMinPlayers;
    }
    public String getDefaulttournamentinvitationcontact() {
        return defaultTournamentInvitationContact;
    }

    public void setDefaulttournamentinvitationcontact(String defaultTournamentInvitationContact) {
        this.defaultTournamentInvitationContact = defaultTournamentInvitationContact;
    }
    public int getMinimalattendance() {
        return minimalAttendance;
    }

    public void setMinimalattendance(int minimalAttendance) {
        this.minimalAttendance = minimalAttendance;
    }
    public int getDefaulttournamentinvitationclosure() {
        return defaultTournamentInvitationClosure;
    }

    public void setDefaulttournamentinvitationclosure(int defaultTournamentInvitationClosure) {
        this.defaultTournamentInvitationClosure = defaultTournamentInvitationClosure;
    }
    public int getDefaultmaxplayers() {
        return defaultMaxPlayers;
    }

    public void setDefaultmaxplayers(int defaultMaxPlayers) {
        this.defaultMaxPlayers = defaultMaxPlayers;
    }

    public List<pokerleague_Player> getPokerleague_players() {
        return pokerleague_players;
    }

    public void addPokerleague_player(Pokerleague_player pokerleague_player) {
        this.pokerleague_players.add(pokerleague_player);
    }
    public pokerleague_PrizeMoneyRuleSet getPokerleague_prizemoneyruleset() {
        return pokerleague_prizemoneyruleset;
    }

    public void setPokerleague_prizemoneyruleset(pokerleague_PrizeMoneyRuleSet pokerleague_prizemoneyruleset) {
        this.pokerleague_prizemoneyruleset = pokerleague_prizemoneyruleset;
    }

}