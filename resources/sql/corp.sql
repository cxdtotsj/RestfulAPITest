CREATE TABLE IF NOT EXISTS `corp_create` (
    `id` VARCHAR(32) PRIMARY KEY NOT NULL,
    `name` VARCHAR(256) NOT NULL DEFAULT '',
    `modify_by` VARCHAR(32) NOT NULL DEFAULT 'SYSTEM',
    `create_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    `update_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP()
);