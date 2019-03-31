# Concern Definition (Calendar)

**Concern-Tag :** `calendar`

This is all about calendar events.

## General Parameters

* **cards** (array) Array of cards
* **card** (dictionary) A specific event
    - Task
    - dueDate

## Request Types

### Cards due on a specific day

**Type-Tag:** `cards_due_day`

#### Request

- **date** (ISO 8601 Timestring): Date to get all events for
- **user**: (string): Internal user id to get associated calendars

#### Response

- **cards**: Array as listed in general parameters


### Cards due until a given date

**Type-Tag:** `cards_due_until`

#### Request

- **date** (ISO 8601 Timestring): Day until all cards should be due
- **user**: (string): Internal user id to get associated calendars

#### Response

- **events**: Array as listed in general parameters

#### Example

Request

```json
{
    "type": "cards_due_until",
    "payload": {
        "user": "AntonHynkel",
        "date": "2007-01-01"
    }
}
```
